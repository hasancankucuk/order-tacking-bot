import { Bot } from "../components/introduction/Bot";
import { DBViewer } from "../components/introduction/DBViewer";
import { Seeding } from "../components/introduction/Seeding";
import { SQLPlayground } from "../components/introduction/SQLPlayground";
import Stepper from "../components/introduction/Stepper";
import { Test } from "../components/introduction/Test";

const Step1 = () => <Bot/>;
const Step2 = () => <DBViewer />;
const Step3 = () => <SQLPlayground />
const Step4 = () => <Test />;
const Step5 = () => <Seeding />;

const steps = [
  "Step 1: Bot Architecture",
  "Step 2: Database Viewer",
  "Step 3: SQL Playground",
  "Step 4: Test Cases",
  "Step 5: Seeding Database",
];

const components = [
  <Bot/>,
  <DBViewer />,
  <SQLPlayground />,
  <Test />,
  <Seeding />
];

export const Introduction = () => {
  return (
     <div className="uk-card uk-card-default uk-card-body uk-margin-top" >
      <h1 className="uk-heading-primary">Introduction</h1>
        <Stepper components={components} steps={steps} />
    </div>
  );
};