import baseurl from "./BASEURL";
import { get_cohort_link } from "./cohorts";

const get_all_instructors = () => {
  return fetch(`${baseurl}instructor`).then((response) => response.json());
};

const get_all_instructors_embedded = () => {
  return fetch(`${baseurl}instructor`)
    .then((response) => response.json());
};

export { get_all_instructors, get_all_instructors_embedded };
