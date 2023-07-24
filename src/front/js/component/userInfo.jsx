import React, { useContext } from "react";
import { Context } from "../store/appContext";

export const UserInfo = () => {
  const { store } = useContext(Context);

  return (
    <div
      className="card mx-auto"
      style={{
        width: "25rem",
        backgroundColor: `hsl(${store.user.color.h},${store.user.color.s}%,${store.user.color.l}%)`,
      }}
    >
      <h2>Username: {store.user.username}</h2>
      <h2>Email: {store.user.email}</h2>
      <h2>
        Favorite Color:{" "}
        {`hsl(${store.user.color.h},${store.user.color.s}%,${store.user.color.l}%)`}
      </h2>
    </div>
  );
};
