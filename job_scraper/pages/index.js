import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/jobs/").then((res) => setJobs(res.data));
  }, []);

  return (
    <div className="p-5">
      <h1 className="text-2xl font-bold">Job Listings</h1>
      <div className="mt-4 grid gap-4">
        {jobs.map((job) => (
          <div key={job.id} className="border p-3 rounded">
            <h2 className="text-xl font-semibold">{job.title}</h2>
            <p>{job.company} - {job.location}</p>
            <a href={job.apply_link} className="text-blue-500">Apply</a>
          </div>
        ))}
      </div>
    </div>
  );
}
