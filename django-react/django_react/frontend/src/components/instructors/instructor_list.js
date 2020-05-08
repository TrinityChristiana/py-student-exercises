import React, { useEffect, useState } from "react";
import { get_all_instructors_embedded } from "../../modules/instructors";
import { render } from "react-dom";
import RegTable from "../tables/RegTable";
import createtable from "../tables/createtableinfo";

/* 




*/

function InstructorList() {
  const [instructors, setInstructors] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");
  const [table_data, setTable_data] = useState({
    data: [],
    columns: [],
  });

  useEffect(() => {
    get_all_instructors_embedded().then((rawdata) => {
      setInstructors(rawdata);
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
      columns_array={table_data.columns}
      data_array={table_data.data}
      title="Instructor Table"
    />
    // <ul>
    //   {instructors.map((i) => {
    //     return (
    //       <li key={i.id}>
    //         {i.first_name} {i.last_name} (@{i.slack_handle})
    //             <ul>
    //                 <li>Is in {i.cohort.name}</li>
    //                 <li>Specializes in {i.specialty}</li>
    //             </ul>
    //       </li>
    //     );
    //   })}
    // </ul>
  );
}

export default InstructorList;
