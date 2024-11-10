import Navbar from "../components/Navbar";
import Chart from "../components/Chart";
import Chart2 from "../components/Specialist";
import Patients from "../components/Patients";
import Schedule from "../components/Schedule"

export default function Dash() {
  return (
    <>
      <Navbar pageType="dash" />
      <div
        style={{
          display: "flex",
          justifyContent: "space-around",
          alignItems: "center",
          paddingTop: "5rem",
          gap: "2rem",
        }}
      >
        <Chart />
        <Chart2 />
        <Patients />
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-around",
          alignItems: "center",
          paddingTop: "2rem",
          gap: "2rem",
        }}
      >
        <Schedule/>
      </div>
    </>
  );
}
