import React from 'react';

const NotFoundPage: React.FC = () => {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">404 - Page Not Found</h1>
      <p>The requested page does not exist.</p>
    </div>
  );
};

export default NotFoundPage;