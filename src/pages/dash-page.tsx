import Navbar from "../components/Navbar";
import Chart from "../components/Chart";
import Chart2 from "../components/Specialist";
import Patients from "../components/Patients";
import Schedule from "../components/Schedule";
import JoinNetwork from "../_components/join-p2p";

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
          paddingLeft: "1 rem",
          paddingRight: "1 rem",
          gap: "1rem",
        }}
      >
        <Chart />
        <Chart2 />
        <JoinNetwork/>
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-around",
          alignItems: "center",
          paddingTop: "2rem",
          paddingBottom: "1rem",
          paddingLeft: "1 rem",
          paddingRight: "1 rem",
          gap: "1.5rem",
        }}
      >
      <Patients />
        <Schedule />
      </div>
    </>
  );
}
