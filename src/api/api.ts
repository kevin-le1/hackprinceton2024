import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
type UUID = string;

interface PATIENT {
    patient_id: UUID;
    patient_name: string;
    information: string;
    specalist: string;
  }

export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000/api/v1", // i am hardcoding
  }),

  tagTypes: ["patient"],
  endpoints: (builder) => ({
    postPatient: builder.mutation<string, { display_name: string }>({
      query: (body) => ({
        url: "/patient",
        method: "POST",
        body: body,
      }),
      invalidatesTags: ["patient"],
    }),
    // TODO: type this
    getPatientAll: builder.query<PATIENT, void>({
      query: () => "/patient/all",
      providesTags: ["patient"],
    }),
    editPatient: builder.mutation<void, { documentId: UUID; data: PATIENT }>({
        query: (data) => ({
            url: `/patient/${data.documentId}`,
            method: "PUT",
            body: data,
            providesTags: ["Documents"],
        })
    }),

    deletePatient: builder.mutation({
      query: (patientID) => ({
        url:`/patient/${patientID}`,
        method: "DELETE",
        invalidatesTags: ["patient"],
      }),
    }),
  }),
});

export default api;
