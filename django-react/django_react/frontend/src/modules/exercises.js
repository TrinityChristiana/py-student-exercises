import baseurl from "./BASEURL"


const get_all_exercises = () => {
    return fetch(`${baseurl}exercise`)
    .then((response) => response.json())
}

export {get_all_exercises};
