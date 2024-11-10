import { useMemo, useState, useEffect } from "react";
import api from "../api/api";
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "../components/ui/table"

const Schedule = () => {
  // indices: 0 is ordering, 1 specialist name, 2 specialist type, 3 patient name, patient uuid
  const { data: specialists } = api.endpoints.getScheduleAll.useQuery();

  // reformats data
  const formattedData = useMemo(() => {
    if (!specialists) return {};

    // Group specialists by type
    const groupedData = specialists.reduce((acc, special) => {
      const [order, specialistName, specialistType, patientName] = special;

      // If the specialist type is not already a key, create an array for it
      if (!acc[specialistType]) {
        acc[specialistType] = [];
      }

      // Push the specialist details into the array for this type
      acc[specialistType].push({
        order,
        specialistName,
        patientName,
      });

      return acc;
    }, {});

    // Sort each specialist type array by specialistName, then by order
    Object.keys(groupedData).forEach((type) => {
      groupedData[type].sort((a, b) => {
        if (a.specialistName === b.specialistName) {
          return a.order - b.order;
        }
        return a.specialistName.localeCompare(b.specialistName);
      });
    });

    return groupedData;
  }, [specialists]);

  const uniqueSpecialists = useMemo(
    () => Object.keys(formattedData),
    [formattedData]
  );

  // State for currently selected specialist type
  const [currentSpecialist, setCurrentSpecialist] = useState("");

  // Set the initial specialist type when formattedData is populated
  useEffect(() => {
    if (uniqueSpecialists.length > 0 && !currentSpecialist) {
      setCurrentSpecialist(uniqueSpecialists[0]);
    }
  }, [uniqueSpecialists, currentSpecialist]);

  const handleSpecialistChange = (event) => {
    setCurrentSpecialist(event.target.value);
  };

  return (
    <div>
      <div style={{ ...styles.dropdown, padding: '8px', border: 'none', outline: 'none', width: '400px' }}>
        <select
          className="text-black bg-white"
          style={{...styles.dropdown}}
          onChange={handleSpecialistChange}
          value={currentSpecialist}
        >
          {uniqueSpecialists.map((specialist, index) => (
            <option key={index} value={specialist}>
              {specialist}
            </option>
          ))}
        </select>
      </div>

      {currentSpecialist && formattedData[currentSpecialist] && (
        <div>
            <Table className = "bg-white rounded-md">
            <TableCaption>The ordering of patients based on their overall ranking.</TableCaption>
            <TableHeader>
                <TableRow>
                <TableHead className="w-[150px]">Specialist Name</TableHead>
                <TableHead className="w-[150px]">Patient Name</TableHead>
                <TableHead className="text-right">Order</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {formattedData[currentSpecialist].map((item, index) => (
                <TableRow key={index}>
                <TableCell className = "text-black">{item.specialistName}</TableCell>
                    <TableCell className="flex text-black">{item.patientName}</TableCell>
                    <TableCell className="font-medium text-right text-black">{item.order}</TableCell>

                </TableRow>
              ))}
            </TableBody>
            </Table>
        </div>
      )}
      
    </div>
  );
};


const styles = {
  dropdownContainer: {
    position: "relative",
    width: "100%",
    fill: "white"
  },
  dropdown: {
    padding: "10px",
    fontSize: "16px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    marginTop: "10px",
    zIndex: 10,
    width: "100%",
    fill: "white"
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "20px",
    color: "#000",
  },
  th: {
    borderBottom: "1px solid #ddd",
    padding: "8px",
  },
  td: {
    borderBottom: "1px solid #ddd",
    padding: "8px",
    textAlign: "left",
  },
};

export default Schedule;

/*
  if (uniqueSpecialists.length == 0 && uniqueSpecialists != undefined) {
    return (
      <div>
        <h2 className="text-black">Select a Specialist</h2>
        <div style={styles.dropdownContainer}>
          <select style={styles.dropdown} disabled>
            <option>No specialists available</option>
          </select>
        </div>
        <table style={styles.table}>
          <thead>
            <tr>
              <th>Data Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>No data</td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
*/
