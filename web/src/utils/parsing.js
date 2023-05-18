export const parsePaginationHeaders = (headers) => {
    const pagination = {};
    for (let [header, value] of headers.entries()) {
      if (header === 'x-pagination-has_next') {
        pagination.hasNext = value === 'True';
      }
      if (header === 'x-pagination-has_prev') {
        pagination.hasPrev = value === 'True';
      }
      if (header === 'x-pagination-page') {
        pagination.page = JSON.parse(value);
      }
      if (header === 'x-pagination-pages') {
        pagination.pages = JSON.parse(value);
      }
      if (header === 'x-pagination-per-page') {
        pagination.perPage = JSON.parse(value);
      }
      if (header === 'x-pagination-total') {
        pagination.total = JSON.parse(value);
      }
    }
    return pagination;
  };
  