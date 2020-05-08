import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import StudentList from "./students/student_list";
import InstructorList from "./instructors/instructor_list";
import CohortList from "./cohorts/cohort_list";
import ExerciseList from "./exercises/exercises_list";
import Dashboard from "./dashboard/dashboard";

const Paths = () => {
  return (
    <div>
      {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
      <Switch>
        <Route path="/students">
          <StudentList />
        </Route>
        <Route path="/instructors"><InstructorList /></Route>
        <Route path="/cohorts"><CohortList/></Route>
        <Route path="/exercises"><ExerciseList/></Route>
        <Route path="/"><Dashboard /></Route>
      </Switch>
    </div>
  );
};

export default Paths;
