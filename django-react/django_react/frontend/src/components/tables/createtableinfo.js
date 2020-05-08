import { get_all_cohorts } from "../../modules/cohorts";

const create_table = (rawdata) => {
  const capitalize = (s) => {
    if (typeof s !== "string") return "";
    return s.charAt(0).toUpperCase() + s.slice(1);
  };

  let columns = [];
  let data = [];

  let promise_array = [];
  for (let prop in rawdata[0]) {
    if (typeof rawdata[0][prop] == "object") {
      if (prop === "cohort") {
        let propmse_1 = get_all_cohorts().then((data) => {
          let column = { title: "Cohort", field: "cohort", lookup: {} };
          data.forEach((cohort) => {
            column.lookup[cohort.id] = cohort.name;
          });
          columns.push(column);
        });
        promise_array.push(propmse_1);
      }
    } else if (prop !== "url") {
      columns.push({
        field: prop,
        title: prop.split("_").map(capitalize).join(" "),
      });
    }
  }

  return Promise.all(promise_array).then(() => {
    rawdata.forEach((element, i) => {
      let newObj = {};
      columns.forEach((field) => {
        if (typeof element[field.field] == "object") {
          newObj[field.field] = element[field.field].id;
        } else {
          newObj[field.field] = element[field.field];
        }
      });
      data.push(newObj);
    });

    return [columns, data];
  });
};

export default create_table;
