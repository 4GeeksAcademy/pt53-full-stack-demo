import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { Card } from "../component/card.jsx";

import "../../styles/home.css";

export const ShipPage = () => {
  const { ship_id } = useParams();
  const [ship, setShip] = useState({});

  useEffect(() => {
    fetch(`https://swapi.dev/api/starships/${ship_id}`)
      .then((resp) => resp.json())
      .then((data) => setShip(data));
  }, []);

  return (
    <div className="text-center mt-5">
      <Card
        img={`https://starwars-visualguide.com/assets/img/starships/${ship_id}.jpg`}
        width="75%"
      >
        <h4 className="card-title">{ship.name}</h4>
        <p className="card-text">
          The {ship.manufacturer} {ship.model} is one of the cooler ships in the
          Star Wars canon.
        </p>
        <ul className="list-group list-group-flush">
          <li className="list-group-item">Length: {ship.length} m</li>
          <li className="list-group-item">Crew count: {ship.crew}</li>
          <li className="list-group-item">
            Passenger count: {ship.passengers}
          </li>
        </ul>
      </Card>
    </div>
  );
};
