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
      user: {
        username: "sombra",
        email: "sombra@catemail.com",
        color: {
          h: 270,
          s: 75,
          l: 50,
        },
      },
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
      changeUserAttrs: (key, val) => {
        let userObj = JSON.parse(JSON.stringify(getStore().user));
        userObj[key] = val;
        setStore({ user: userObj });
      },

      changeMessage: () => {
        setStore({
          message:
            "This library went to meet the great Amiga in the sky.  I'm sorry Timmy.",
        });
      },

      exampleFunction: () => {
        getActions().changeColor(0, "green");
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
