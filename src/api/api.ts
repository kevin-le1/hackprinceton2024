import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
type UUID = string;

// patient_id, patient_name, specialist_type, risk_score, bmi, heart_rate, blood_pressure
interface Patient {
    patient_id: UUID;
    patient_name: string;
    bmi: string;
    heart_rate:string;
    blood_pressure:string;
    specialist_type: string;
    risk_score: string;
    age: string;
    hoshospitalizations_in_last_year:string;
    previous_surgeries:string;
    cholestoral_level:string;
    respiratory_rate:string;
  }

export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1", // i am hardcoding
  }),

  tagTypes: ["Patient"],
  endpoints: (builder) => ({
    postPatient: builder.mutation<void, void>({
      query: () => ({
        url: "/patient/",
        method: "POST",
        body: {},
      }),
      invalidatesTags: ["Patient"],
    }),
    // TODO: type this
    getPatientAll: builder.query<Patient[], void>({
      query: () => "/patient/all",
      providesTags: ["Patient"],
    }),
    editPatient: builder.mutation<void, { data: Patient }>({
        query: (data) => ({
            url: `/patient/`,
            method: "PUT",
            body: data,
            invalidatesTags: ["Patient"],
        })
    }),

    deletePatient: builder.mutation({
      query: (patientID) => ({
        url:`/patient/${patientID}`,
        method: "DELETE",
        invalidatesTags: ["Patient"],
      }),
    }),
    startInference: builder.mutation<void, void>({
        query: () => ({
          url: "/patient/inference",
          method: "POST",
          body: {},
        }),
        invalidatesTags: ["Patient"],
      }),
    }),
    
    // PART FOR DASHBOARD


});

export default api;
