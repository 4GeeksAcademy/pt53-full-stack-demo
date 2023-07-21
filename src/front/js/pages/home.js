import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Card } from "../component/card.jsx";
import { Link } from "react-router-dom";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="text-center mt-5">
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
