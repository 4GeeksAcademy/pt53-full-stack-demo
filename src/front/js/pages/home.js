import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Card } from "../component/card.jsx";
import { Link } from "react-router-dom";
import { UserInfo } from "../component/userInfo.jsx";
import { LoginForm } from "../component/login.jsx";

export const Home = () => {
  const { store, actions } = useContext(Context);
  const [user, setUser] = useState("");
  const [email, setEmail] = useState("");
  const [hue, setHue] = useState("");

  const [ships, setShips] = useState([]);

  // useEffect(() => {
  //   setUser(store.user.username);
  //   setEmail(store.user.email);
  //   setHue(store.user.color.h);
  // }, []);

  // useEffect(() => {
  //   actions.changeUserAttrs("username", user);
  //   actions.changeUserAttrs("email", email);
  //   actions.changeUserAttrs("color", {
  //     h: parseInt(hue),
  //     s: store.user.color.s,
  //     l: store.user.color.l,
  //   });
  // }, [user, email, hue]);

  useEffect(async () => {
    const resps = await Promise.all(
      ["starships", "planets"].map((url) =>
        fetch(`https://swapi.dev/api/${url}`)
      )
    );
    const jsonData = await Promise.all(resps.map((resp) => resp.json()));

    for (let data of jsonData) {
      if (data.next.split("/").includes("starships")) {
        setShips(data.results);
      }
    }
  }, []);

  return (
    <div className="text-center mt-5">
      <Card>token: {JSON.stringify(store.user)}</Card>
      <button className="btn btn-primary" onClick={actions.get_identity}>
        Get User Data
      </button>
      <LoginForm />
      {/* <UserInfo /> */}
      {/* <div className="card mx-auto" style={{ width: "25rem" }}>
        <label>
          Username:
          <input value={user} onChange={(ev) => setUser(ev.target.value)} />
        </label>
        <label>
          Email:
          <input value={email} onChange={(ev) => setEmail(ev.target.value)} />
        </label>
        <label>
          Hue:
          <input value={hue} onChange={(ev) => setHue(ev.target.value)} />
        </label>
      </div> */}
      {/* {ships.map((ship, idx) => (
        <Card
          img={`https://starwars-visualguide.com/assets/img/starships/${
            ship.url.split("/")[5]
          }.jpg`}
          key={idx}
        >
          <h4 className="card-title">{ship.name}</h4>
          <p className="card-text">
            The {ship.manufacturer} {ship.model} is one of the cooler ships in
            the Star Wars canon.
          </p>
          <ul className="list-group list-group-flush">
            <li className="list-group-item">Length: {ship.length} m</li>
            <li className="list-group-item">Crew count: {ship.crew}</li>
            <li className="list-group-item">
              Passenger count: {ship.passengers}
            </li>
            <li className="list-group-item">
              <Link to={`/ships/${ship.url.split("/")[5]}`}>
                <button className="btn btn-primary">Learn More!</button>
              </Link>
            </li>
          </ul>
        </Card>
      ))} */}
    </div>
  );
};
