import React from 'react';

interface JobCardProps {
  // Define props here
}

const JobCard: React.FC<JobCardProps> = ({}) => {
  return (
    <div className="p-4 border rounded-lg">
      <h3>JobCard Component</h3>
      <p>Job card content goes here</p>
    </div>
  );
};

export default JobCard;