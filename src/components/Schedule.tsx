import { useMemo } from 'react';
import api from "../api/api";

const Schedule = () => {

    // Gets data
    const { data: patients } = api.endpoints.getPatientAll.useQuery();

    

    // map this afterwards each patient to specialist
    const formattedData = useMemo(() => {
        if (!patients) return [];

        return patients
        .map((patient) => {
            console.log(patient);
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

    console.log(formattedData);

    // Get unique specialist types
    const uniqueSpecialists = useMemo(() => {
        const specialists = formattedData.map((item) => item.specialist);
        return Array.from(new Set(specialists));
    }, [formattedData]);

    console.log(uniqueSpecialists);

  return (
    <div>hi</div>
  );
};


export default Schedule;
