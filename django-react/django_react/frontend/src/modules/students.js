import baseurl from "./BASEURL";
import { get_cohort } from "./cohorts";

const get_all_students = () => {
  return fetch(`${baseurl}student`).then((response) => response.json());
};

const get_all_students_embedded = () => {
  return fetch(`${baseurl}student`)
    .then((response) => response.json())
    .then((data) => {
      let promise_array = [];
      data.forEach((student) => {
        promise_array.push(get_cohort(student.cohort));
      });
      return Promise.all(promise_array).then((values) => {
        data.forEach((student, i) => {
          data[i].cohort = values[i].name;
        });

        return data;
      });
    });
};

export { get_all_students, get_all_students_embedded };
