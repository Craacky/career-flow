import React from 'react';

interface EmptyStateProps {
  message?: string;
  icon?: React.ReactNode;
}

const EmptyState: React.FC<EmptyStateProps> = ({ 
  message = 'No data available', 
  icon 
}) => {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      {icon && <div className="mb-4">{icon}</div>}
      <p className="text-gray-500">{message}</p>
    </div>
  );
};

export default EmptyState;