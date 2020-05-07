import baseurl from "./BASEURL";

const get_all_cohorts = () => {
  return fetch(`${baseurl}cohort`).then((response) => response.json());
};

const get_cohort = (cohort_id) => {
  return fetch(`${baseurl}cohort/${cohort_id}`).then((resp) => resp.json());
};

export { get_all_cohorts, get_cohort };
