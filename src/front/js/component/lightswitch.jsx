import React, { useState, useEffect } from "react";
import lighbulb_on from "../../img/lightbulb_on.png";
import lighbulb_off from "../../img/lightbulb_off.png";

export const LightSwitch = () => {
  const [clapOn, setClapOn] = useState(false);
  const styleObj = {
    width: "80%",
    maxWidth: "30rem",
  };

  useEffect(() => {
    // console.log("https://www.youtube.com/watch?v=Ny8-G8EoWOw");
    console.log("Current value of clapOn:", clapOn);
  }, [clapOn]);

  return (
    <div
      data-bs-theme={clapOn ? "light" : "dark"}
      className="card mx-auto my-3"
      style={{
        width: "80%",
        maxWidth: "30rem",
      }}
      onClick={() => setClapOn(!clapOn)}
    >
      <img src={clapOn ? lighbulb_on : lighbulb_off} className="card-img-top" />
      <div className="card-body">
        <h5 className="card-title">Dynamic Lightbulb</h5>
        <p className="card-text">
          <a href="https://thenounproject.com/maxim221/">
            Lightbulb images courtesy Maxim Kulikov.
          </a>
        </p>
      </div>
    </div>
  );
};
