export const getSearchParam = (key=null) => {
    const params = new window.URLSearchParams(window.location.search);
    if (!key) return params;
    return params.get(key) || null
  };