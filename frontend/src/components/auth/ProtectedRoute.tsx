import React from 'react';

interface ProtectedRouteProps {
  // Define props here
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({}) => {
  return (
    <div className="p-4">
      <h3>ProtectedRoute Component</h3>
      <p>Protected route content goes here</p>
    </div>
  );
};

export default ProtectedRoute;