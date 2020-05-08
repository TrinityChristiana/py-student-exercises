import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import CohortList from "../cohorts/cohort_list";
import ExerciseList from "../exercises/exercises_list";
import InstructorList from "../instructors/instructor_list";
import StudentList from "../students/student_list";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
}));

const Dashboard = () => {
  const classes = useStyles();
  const [items, setItems] = useState([
    <CohortList />,
    <ExerciseList />,
    <InstructorList />,
    <StudentList />,
  ]);
  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        {items.map((item) => (
          <Grid item lg={6} md={12}>
            {item}
          </Grid>
        ))}
      </Grid>
    </div>
  );
};

export default Dashboard;
