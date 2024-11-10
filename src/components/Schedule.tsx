import { useMemo, useState } from 'react';
import api from "../api/api";


const Schedule = () => {

    // Gets data
    const { data: patients } = api.endpoints.getPatientAll.useQuery();
    const { data: specialists } = api.endpoints.getScheduleAll.useQuery();
    
    console.log(specialists);

    // map this afterwards each patient to specialist
    const formattedData = useMemo(() => {
        if (!patients) return [];

        return patients
        .map((patient) => {
            const patient_name = patient[1];
            const specialist_type = patient[2];
            const uuid = patient[0];
            return {
            uuid: uuid,
            name: patient_name,
            specialist: specialist_type,
            };
        })
    }, [patients]);


    // Get unique specialist types
    const uniqueSpecialists = useMemo(() => {
        const specialists = formattedData.map((item) => item.specialist);
        return Array.from(new Set(specialists));
    }, [formattedData]);

    const [currentSpecialist, setCurrentSpecialist] = useState(uniqueSpecialists.length > 0 ? uniqueSpecialists[0] : '');

    const handleSpecialistChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setCurrentSpecialist(event.target.value);
    };


    if (uniqueSpecialists.length == 0 && uniqueSpecialists != undefined) {
        
        return (
            <div>
                <h2>Select a Specialist</h2>
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



    console.log(currentSpecialist);


    return (
        <div>
            <h2>Select a Specialist</h2>
            <div style={styles.dropdownContainer}>
            <select style={styles.dropdown} onChange={handleSpecialistChange}>
                {uniqueSpecialists.map((specialist, index) => (
                <option key={index} value={specialist}>
                    {specialist}
                </option>
                ))}
            </select>
            {currentSpecialist ? currentSpecialist : uniqueSpecialists[0]}
            </div>
        </div>
    );
};
    
const styles = {
    dropdownContainer: {
    position: 'relative',
    width: '100%',
    },
    dropdown: {
    padding: '10px',
    fontSize: '16px',
    borderRadius: '5px',
    border: '1px solid #ccc',
    marginTop: '10px',
    zIndex: 10,
    width: '100%',
    },
};


export default Schedule;
