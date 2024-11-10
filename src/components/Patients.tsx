import { useMemo } from "react";
import api from "../api/api";

const Patients = () => {
  const { data: patients } = api.endpoints.getPatientAll.useQuery();

  const formattedData = useMemo(() => {
    if (!patients) return [];

    return (
      patients
        .map((patient) => {
          const patient_name = patient[1];
          const risk_score = patient[4] ? parseFloat(patient[3]) : 1;

          // Determine health status based on risk_score
          let healthStatus;
          if (risk_score >= 0 && risk_score < 0.4) {
            healthStatus = "Healthy";
          } else if (risk_score >= 0.4 && risk_score < 0.7) {
            healthStatus = "Sick";
          } else if (risk_score >= 0.7 && risk_score <= 1) {
            healthStatus = "Heavily ill";
          } else {
            healthStatus = "Unknown";
          }

          return {
            name: patient_name,
            email: healthStatus,
            amount: risk_score,
          };
        })
        // Sort from lowest to greatest
        .sort((a, b) => b.amount - a.amount)
    );
  }, [patients]);

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Patient Risk Scores</h2>
      <p style={styles.subHeader}>
        A higher score indicates a higher risk of illness.
      </p>
      <ul style={styles.list}>
        {formattedData.map((sale, index) => (
          <li key={index} style={styles.listItem}>
            <div style={styles.infoContainer}>
              <span style={styles.name}>{sale.name}</span>
              <span style={styles.email}>{sale.email}</span>
            </div>
            <span style={styles.amount}>{sale.amount}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

const styles = {
  container: {
    backgroundColor: "#FFF",
    padding: "20px",
    borderRadius: "12px",
    minWidth: "650px",
    maxHeight: "340px",
    color: "#000",
  },
  header: {
    fontSize: "20px",
    fontWeight: "600",
    marginBottom: "8px",
    color: "#000",
  },
  subHeader: {
    fontSize: "16px",
    color: "#000",
    marginBottom: "16px",
  },
  list: {
    listStyleType: "none",
    padding: 0,
    margin: 0,
    maxHeight: "230px",
    overflowY: "auto",
  },
  listItem: {
    color: "#000",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "12px 0",
    borderBottom: "1px solid #333",
  },
  infoContainer: {
    display: "flex",
    flexDirection: "column",
  },
  name: {
    fontSize: "16px",
    fontWeight: "500",
  },
  email: {
    fontSize: "14px",
    color: "#111",
  },
  amount: {
    fontSize: "16px",
    fontWeight: "500",
  },
};

export default Patients;
