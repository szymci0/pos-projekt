import {encode} from 'querystring';
import {parsePaginationHeaders} from './parsing';
import {ActiveUser} from "@/services/user";

export const redirectIfNotAuthenticated = (res) => {
  if (res.status === 401) {
    ActiveUser.clear();
    window.localStorage.setItem('pathToLoadAfterLogin', window.location.pathname);
    return window.location.replace('/account/login');
  }
  if (res.status === 403)
    return window.location.replace('/');
};

export const request = async ({
      url,
      query,
      headers = {},
      method = 'GET',
      body,
      formData,
      skipRedirect = false,
      ...rest
    }) => {
  const methodLower = method.toLowerCase();
  if (
    body &&
    (methodLower === 'post' ||
      methodLower === 'put' ||
      methodLower === 'patch' ||
      methodLower === 'delete') &&
    !headers['Content-Type']
  ) {
    headers['Content-Type'] = 'application/json';
  }
  if (body && typeof body === 'object') {
    body = JSON.stringify(body);
  }
  if (formData) {
    body = formData;
  }
  const token = ActiveUser.getToken();
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  const res = await fetch(url + (query ? `?${encode(query)}` : ''), {
    method,
    headers,
    body,
    ...rest,
  });

  if (!skipRedirect) {
    redirectIfNotAuthenticated(res);
  }

  const contentType = res.headers.get('content-type');
  if (contentType !== 'application/json') {
    return {
      res,
      data: {},
      pagination: {},
      headers: res.headers,
    };
  }

  const data = await res.json();
  const pagination = parsePaginationHeaders(res.headers);

  return {
    res,
    data,
    pagination,
    headers: res.headers,
  };
};

export const getFileNameFromHeaders = (headers) => {
  return headers
    .get("content-disposition")
    ?.split("filename=")
    .pop()
    .replaceAll('"', "");
};

export const downloadFile = async ({
  fileName,
  downloadURL,
  headers = {},
  method = "GET",
  query = null,
  body = null,
}) => {
  headers["Content-Type"] = "application/json";
  headers["Authorization"] = `Bearer ${ActiveUser.getToken()}`;
  headers["Cache-Control"] = "no-cache";
  downloadURL = `${downloadURL}?${encode(query)}`;

  if (body && method === "POST") {
    body = JSON.stringify(body);
  }

  const response = await fetch(downloadURL, {
    method,
    headers,
    body,
  });
  if (response.status !== 200) {
    return alert("File not found");
  }
  fileName = fileName || getFileNameFromHeaders(response.headers);
  const fileResponse = await response.blob();
  const objectUrl = window.URL.createObjectURL(fileResponse);
  const anchor = document.createElement("a");

  document.body.appendChild(anchor);
  anchor.href = objectUrl;
  anchor.download = fileName;
  anchor.click();

  window.URL.revokeObjectURL(objectUrl);
  anchor.remove();
};