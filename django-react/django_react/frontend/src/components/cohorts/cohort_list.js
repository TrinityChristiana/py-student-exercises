import React, { useEffect, useState } from "react";
import { get_all_cohorts } from "../../modules/cohorts";
import { render } from "react-dom";
import RegTable from "../tables/RegTable";
import createtable from "../tables/createtableinfo";

function ExerciseList() {
  const [cohorts, setCohorts] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");
  const [table_data, setTable_data] = useState({
    data: [],
    columns: [],
  });

  useEffect(() => {
    get_all_cohorts().then((rawdata) => {
      setCohorts(rawdata);
      setLoaded(true);
      createtable(rawdata).then(([columns, data]) => {
        setTable_data((prevstate) => {
          let newObj = { ...prevstate };
          newObj.data = data;
          newObj.columns = columns;
          return newObj;
        });
      });
    });
  }, []);

  return (
    <RegTable
      options={{
        exportButton: true,
      }}
      title="Cohort Table"
      columns_array={table_data.columns}
      data_array={table_data.data}
    />
  );
}

export default ExerciseList;
