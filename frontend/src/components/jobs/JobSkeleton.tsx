import React from 'react';

interface JobSkeletonProps {
  // Define props here
}

const JobSkeleton: React.FC<JobSkeletonProps> = ({}) => {
  return (
    <div className="p-4 animate-pulse">
      <h3>JobSkeleton Component</h3>
      <p>Loading skeleton for job content</p>
    </div>
  );
};

export default JobSkeleton;