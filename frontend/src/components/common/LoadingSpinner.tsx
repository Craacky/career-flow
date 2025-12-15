import React from 'react';

interface LoadingSpinnerProps {
  // Define props here
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({}) => {
  return (
    <div className="flex justify-center items-center">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
    </div>
  );
};

export default LoadingSpinner;