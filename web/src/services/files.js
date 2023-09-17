import { ActiveUser } from "./user";
import { redirectIfNotAuthenticated } from "@/utils/request";

class Files {
    uploadFile({
        file,
        fileId = null,
        onProgress = null,
        url = null,
        onError = () => {},
    }) {
        return new Promise((resolve, reject) => {
            const uploadedFilename = file.name;
            const formData = new FormData();
            formData.append('file', file, uploadedFilename);
            formData.append('file_id', fileId);
            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = () => {
              if (xhr.readyState === 4) {
                onProgress && onProgress(100);
                if (xhr.status === 200) {
                  resolve('File was uploaded successfully.');
                } else {
                  redirectIfNotAuthenticated(xhr);
                  try {
                    const response = JSON.parse(xhr.responseText);
                    if (onError) onError(response)
                    else reject(`Error occurred during upload. ${response?.detail?.message}.`);
                  } catch {
                    reject('Error occurred during upload.');
                  }
                }
              }
            };
      
            xhr.onprogress = function (e) {
              if (e.lengthComputable) {
                onProgress && onProgress(e.loaded / e.total * 100);
              }
            };
            onProgress && onProgress(0);
      
            xhr.open('post', url);
            xhr.setRequestHeader('authorization', `Bearer ${ActiveUser.getToken()}`);
            xhr.send(formData);
          });
    }
}

export const FilesService = new Files();