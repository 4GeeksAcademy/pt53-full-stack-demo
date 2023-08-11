import React, { useState, useContext } from "react";
import { Context } from "../store/appContext.js";
import { Card } from "./card.jsx";

export const LoginForm = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [success, setSuccess] = useState(true);

  const handleSubmit = async (ev) => {
    ev.preventDefault();
    setSuccess(await actions.login(email, pass));
    setEmail("");
    setPass("");

    console.log(store);
  };

  return (
    <Card>
      <form onSubmit={handleSubmit}>
        {success ? "" : store.message}

        <label>email:</label>
        <input
          type="email"
          value={email}
          onChange={(ev) => setEmail(ev.target.value)}
        />

        <label>password:</label>
        <input
          type="password"
          value={pass}
          onChange={(ev) => setPass(ev.target.value)}
        />

        <button className="btn btn-primary">Login</button>
      </form>
    </Card>
  );
};
