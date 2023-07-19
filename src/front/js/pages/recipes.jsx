import React from "react";

import { Card } from "../component/card.jsx";
import { LightSwitch } from "../component/lightswitch.jsx";

export const RecipesPage = () => {
  return (
    <div className="container">
      <Card width="24rem">
        <h1>Aeblekage</h1>
        <h2>Ingredients</h2>
        <p>An apple trifle from Denmark. Super tasty.</p>
        <ul>
          <li>1 large jar applesauce</li>
          <li>1.5c breadcrumbs (Panko works fine)</li>
          <li>1 pint heavy or whipping cream</li>
          <li>1 tsp vanilla extract</li>
          <li>Cinnamon</li>
          <li>Sugar</li>
          <li>Butter</li>
        </ul>

        <h2>Steps</h2>
        <ul>
          <li>...</li>
          <li>You get the idea</li>
          <li>Although I will probably fill this out later.</li>
        </ul>
      </Card>
      <Card width="24rem">
        <h1>Aeblekage</h1>
        <h2>Ingredients</h2>
        <p>An apple cake from Denmark. Super tasty.</p>
        <ul>
          <li>I might also put in this recipe.</li>
        </ul>

        <h2>Steps</h2>
        <ul>
          <li>...</li>
          <li>You get the idea</li>
          <li>Although I will probably fill this out later.</li>
        </ul>
      </Card>
      <LightSwitch />
    </div>
  );
};
