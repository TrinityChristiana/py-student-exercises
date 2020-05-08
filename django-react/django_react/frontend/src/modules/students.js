import baseurl from "./BASEURL";
import { get_cohort_link } from "./cohorts";

const get_all_students = () => {
  return fetch(`${baseurl}student`).then((response) => response.json());
};

const get_all_students_embedded = () => {
  return fetch(`${baseurl}student`)
    .then((response) => response.json());
};

export { get_all_students, get_all_students_embedded };
