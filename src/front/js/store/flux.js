const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      message:
        "This is a test of an old library that was sent to a farm and super happy we swear.",
      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
      ships: [
        {
          name: "B-wing",
          model: "A/SF-01 B-wing starfighter",
          manufacturer: "Slayn & Korpil",
          cost_in_credits: "220000",
          length: "16.9",
          max_atmosphering_speed: "950",
          crew: "1",
          passengers: "0",
          cargo_capacity: "45",
          consumables: "1 week",
          hyperdrive_rating: "2.0",
          MGLT: "91",
          starship_class: "Assault Starfighter",
          pilots: [],
          films: ["https://swapi.dev/api/films/3/"],
          created: "2014-12-18T11:18:04.763000Z",
          edited: "2014-12-20T21:23:49.909000Z",
          url: "https://swapi.dev/api/starships/29/",
        },
      ],
    },
    actions: {
      changeMessage: () => {
        setStore({
          message:
            "This library went to meet the great Amiga in the sky.  I'm sorry Timmy.",
        });
      },

      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },

      getMessage: async () => {
        try {
          // fetching data from the backend
          const resp = await fetch(process.env.BACKEND_URL + "/api/hello");
          const data = await resp.json();
          setStore({ message: data.message });
          // don't forget to return something, that is how the async resolves
          return data;
        } catch (error) {
          console.log("Error loading message from backend", error);
        }
      },

      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
    },
  };
};

export default getState;
