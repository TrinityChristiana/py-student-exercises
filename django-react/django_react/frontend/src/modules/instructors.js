import baseurl from "./BASEURL";
import { get_cohort } from "./cohorts";

const get_all_instructors = () => {
  return fetch(`${baseurl}instructor`).then((response) => response.json());
};

const get_all_instructors_embedded = () => {
  return fetch(`${baseurl}instructor`)
    .then((response) => response.json())
    .then((data) => {
      let promise_array = [];
      data.forEach((instructor) => {
        promise_array.push(get_cohort(instructor.cohort));
      });
      return Promise.all(promise_array).then((values) => {
        data.forEach((instructor, i) => {
          data[i].cohort = values[i].name;
        });
        return data;
      });
    });
};

export { get_all_instructors, get_all_instructors_embedded };
