import React, { useEffect, useState } from "react";
import { get_all_cohorts } from "../../modules/cohorts";
import { render } from "react-dom";

function ExerciseList() {
  const [cohorts, setCohorts] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");

  useEffect(() => {
    get_all_cohorts().then((data) => {
      setCohorts(data);
      setLoaded(true);
    });
  }, []);

  return (
    <ul>
      {cohorts.map((c) => {
        return (
          <li key={c.id}>
            {c.name}
          </li>
        );
      })}
    </ul>
  );
}

export default ExerciseList;
