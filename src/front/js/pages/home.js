import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Card } from "../component/card.jsx";
import { Link } from "react-router-dom";
import { UserInfo } from "../component/userInfo.jsx";
import { LoginForm } from "../component/login.jsx";

const FakeUpload = ({ callback }) => {
  const [f, setF] = useState(null);

  return (
    <div>
      <input
        type="file"
        onChange={(ev) => {
          ev.preventDefault();
          ev.stopPropagation();
          console.log(f);
          setF(ev.target.files[0]);
          console.log(f);
        }}
      />
      <button className="btn btn-primary" onClick={() => callback(f)}>
        This button does things.
      </button>
    </div>
  );
};

export const Home = () => {
  const { store, actions } = useContext(Context);
  const [showFileUpload, setShowFileUpload] = useState(false);
  const [file, setFile] = useState(null);

  const fakeUpload = (f) => {
    setFile(f);
    setShowFileUpload(false);
  };

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
      <button
        className={
          showFileUpload ? "btn btn-primary hidden" : "btn btn-primary"
        }
        onClick={() => setShowFileUpload(true)}
      >
        Upload File
      </button>
      {showFileUpload ? <FakeUpload callback={fakeUpload} /> : ""}
    </div>
  );
};
