import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Card } from "../component/card.jsx";
import { Link } from "react-router-dom";
import { UserInfo } from "../component/userInfo.jsx";

export const Home = () => {
  const { store, actions } = useContext(Context);
  const [user, setUser] = useState("");
  const [email, setEmail] = useState("");
  const [hue, setHue] = useState("");

  useEffect(() => {
    setUser(store.user.username);
    setEmail(store.user.email);
    setHue(store.user.color.h);
  }, []);

  useEffect(() => {
    actions.changeUserAttrs("username", user);
    actions.changeUserAttrs("email", email);
    actions.changeUserAttrs("color", {
      h: parseInt(hue),
      s: store.user.color.s,
      l: store.user.color.l,
    });
  }, [user, email, hue]);

  return (
    <div className="text-center mt-5">
      <UserInfo />
      <div className="card mx-auto" style={{ width: "25rem" }}>
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
      </div>
      {store.ships.map((ship, idx) => (
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
      ))}
    </div>
  );
};
