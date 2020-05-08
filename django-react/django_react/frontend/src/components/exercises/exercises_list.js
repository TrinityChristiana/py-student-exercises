import React, { useEffect, useState } from "react";
import { get_all_exercises } from "../../modules/exercises";
import RegTable from "../tables/RegTable";
import createtable from "../tables/createtableinfo";

function ExerciseList() {
  const [exercises, setExercises] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");
  const [table_data, setTable_data] = useState({
    data: [],
    columns: [],
  });

  useEffect(() => {
    get_all_exercises().then((rawdata) => {
      setExercises(rawdata);
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
    <RegTable options={{
      exportButton: true,
    }} title="Exercise Table" columns_array={table_data.columns} data_array={table_data.data} />
  );
}

export default ExerciseList;
