import React, { forwardRef, useState, useEffect } from "react";
import AddBox from "@material-ui/icons/AddBox";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import Check from "@material-ui/icons/Check";
import ChevronLeft from "@material-ui/icons/ChevronLeft";
import ChevronRight from "@material-ui/icons/ChevronRight";
import Clear from "@material-ui/icons/Clear";
import DeleteOutline from "@material-ui/icons/DeleteOutline";
import Edit from "@material-ui/icons/Edit";
import FilterList from "@material-ui/icons/FilterList";
import FirstPage from "@material-ui/icons/FirstPage";
import LastPage from "@material-ui/icons/LastPage";
import Remove from "@material-ui/icons/Remove";
import SaveAlt from "@material-ui/icons/SaveAlt";
import Search from "@material-ui/icons/Search";
import ViewColumn from "@material-ui/icons/ViewColumn";
// typings are here:
import MaterialTable, { Icons } from "material-table";

const tableIcons: Icons = {
  Add: forwardRef((props, ref) => <AddBox {...props} ref={ref} />),
  Check: forwardRef((props, ref) => <Check {...props} ref={ref} />),
  Clear: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
  Delete: forwardRef((props, ref) => <DeleteOutline {...props} ref={ref} />),
  DetailPanel: forwardRef((props, ref) => (
    <ChevronRight {...props} ref={ref} />
  )),
  Edit: forwardRef((props, ref) => <Edit {...props} ref={ref} />),
  Export: forwardRef((props, ref) => <SaveAlt {...props} ref={ref} />),
  Filter: forwardRef((props, ref) => <FilterList {...props} ref={ref} />),
  FirstPage: forwardRef((props, ref) => <FirstPage {...props} ref={ref} />),
  LastPage: forwardRef((props, ref) => <LastPage {...props} ref={ref} />),
  NextPage: forwardRef((props, ref) => <ChevronRight {...props} ref={ref} />),
  PreviousPage: forwardRef((props, ref) => (
    <ChevronLeft {...props} ref={ref} />
  )),
  ResetSearch: forwardRef((props, ref) => <Clear {...props} ref={ref} />),
  Search: forwardRef((props, ref) => <Search {...props} ref={ref} />),
  SortArrow: forwardRef((props, ref) => <ArrowUpward {...props} ref={ref} />),
  ThirdStateCheck: forwardRef((props, ref) => <Remove {...props} ref={ref} />),
  ViewColumn: forwardRef((props, ref) => <ViewColumn {...props} ref={ref} />),
};

const default_columns = [
  { title: "First Name", field: "first_name" },
  { title: "Last Name", field: "last_name" },
  { title: "Birth Year", field: "birthYear", type: "numeric" },
  {
    title: "Birth Place",
    field: "birthCity",
    lookup: { 37013: "Antioch", 37011: "Nashville" },
  },
];

const default_data = [
  {
    first_name: "Trinity",
    last_name: "Terry",
    birthYear: 1999,
    birthCity: 37013,
  },
  {
    first_name: "Olivia",
    last_name: "Terry",
    birthYear: 2009,
    birthCity: 37011,
  },
];

const RegTable = ({
  title = "Editable Title",
  columns_array = default_columns,
  data_array = default_data,
  update_data = null,
  options,
  detailPanel = true,
}) => {
  const [columns, setColumns] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    setColumns(columns_array);
  }, [columns_array]);

  useEffect(() => {
    setData(data_array);
  }, [data_array]);

  return (
    <MaterialTable
      icons={tableIcons}
      title={title}
      columns={columns}
      //   data={query =>
      //     new Promise((resolve, reject) => {
      //       let url = 'http://localhost:8000/api/student/'

      //       fetch(url)
      //         .then(response => response.json())
      //         .then(result => {
      //           resolve({
      //             data: result,

      //           })
      //         })
      //     })
      //   }
      data={data}
      options={options}
      detailPanel={
        detailPanel &&
        ((rowData) => {
          return (
            <iframe
              width="100%"
              height="315"
              src="https://www.youtube.com/embed/C0DPdy98e4c"
              frameborder="0"
              allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
            />
          );
        })
      }
      onRowClick={
        detailPanel && ((event, rowData, togglePanel) => togglePanel())
      }
      editable={{
        onRowAdd: (newData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();

              setData((prevState) => {
                const data = [...prevState];
                data.push(newData);
                update_data && update_data(data);
                return data;
              });
            }, 600);
          }),
        onRowUpdate: (newData, oldData) =>
          new Promise((resolve, reject) => {
            setTimeout(() => {
              {
                setData((prevState) => {
                  const data = [...prevState];
                  const index = data.indexOf(oldData);
                  data[index] = newData;
                  update_data && update_data(data);
                  return data;
                });
              }
              resolve();
            }, 1000);
          }),
        onRowDelete: (oldData) =>
          new Promise((resolve) => {
            setTimeout(() => {
              resolve();
              setData((prevState) => {
                const data = [...prevState];
                data.splice(data.indexOf(oldData), 1);
                update_data && update_data(data);
                return data;
              });
            }, 600);
          }),
      }}
    />
  );
};

export default RegTable;
