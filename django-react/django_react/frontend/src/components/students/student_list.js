import React, { useEffect, useState } from "react";
import { get_all_students_embedded } from "../../modules/students";
import { render } from "react-dom";

function StudentList() {
  const [students, setStudents] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");

  useEffect(() => {
    get_all_students_embedded().then((data) => {
      setStudents(data);
      setLoaded(true);
    });
  }, []);

  return (
    <ul>
      {students.map((s) => {
        return (
          <li key={s.id}>
            {s.first_name} {s.last_name} @{s.slack_handle}
            <ul>
              <li>Is in {s.cohort}</li>
            </ul>
          </li>
        );
      })}
    </ul>
  );
}

export default StudentList;
