import React, { useEffect, useState } from "react";
import { get_all_instructors_embedded } from "../../modules/instructors";
import { render } from "react-dom";

function InstructorList() {
  const [instructors, setInstructors] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");

  useEffect(() => {
    get_all_instructors_embedded().then((data) => {
        setInstructors(data);
      setLoaded(true);
    });
  }, []);

  return (
    <ul>
      {instructors.map((i) => {
        return (
          <li key={i.id}>
            {i.first_name} {i.last_name} (@{i.slack_handle}) 
                <ul>
                    <li>Is in {i.cohort}</li>
                    <li>Specializes in {i.specialty}</li>
                </ul>
          </li>
        );
      })}
    </ul>
  );
}

export default InstructorList;
