import React, { useEffect, useState } from "react";
import { get_all_students_embedded } from "../../modules/students";
import RegTable from "../tables/RegTable";
import createtable from "../tables/createtableinfo";
function StudentList() {
  const [students, setStudents] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");
  const [table_data, setTable_data] = useState({
    data: [],
    columns: [],
  });

  useEffect(() => {
    get_all_students_embedded().then((rawdata) => {
      setStudents(rawdata);
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
    <>
      <RegTable
        options={{
          filtering: true,
          exportButton: true,
        }}
        columns_array={table_data.columns}
        data_array={table_data.data}
        title="Student Table"
      />
    </>
  );
}

export default StudentList;
