import React, { useEffect, useState } from "react";
import { get_all_exercises } from "../../modules/exercises";
import { render } from "react-dom";

function ExerciseList() {
  const [exercises, setExercises] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [placeholder, setPlaceholder] = useState("Loading");

  useEffect(() => {
    get_all_exercises().then((data) => {
      setExercises(data);
      setLoaded(true);
    });
  }, []);

  return (
    <ul>
      {exercises.map((e) => {
        return (
          <li key={e.id}>
            {e.name} -- {e.language} Exercise
          </li>
        );
      })}
    </ul>
  );
}

export default ExerciseList;
