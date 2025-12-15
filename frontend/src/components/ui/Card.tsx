import React from 'react';

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  title?: string;
  subtitle?: string;
}

const Card: React.FC<CardProps> = ({ title, subtitle, children, className = '', ...props }) => {
  return (
    <div 
      className={`rounded-xl border bg-white shadow-sm overflow-hidden ${className}`} 
      {...props}
    >
      {(title || subtitle) && (
        <div className="p-6 pb-4">
          {title && <h3 className="text-xl font-semibold text-gray-900">{title}</h3>}
          {subtitle && <p className="text-sm text-gray-500 mt-1">{subtitle}</p>}
        </div>
      )}
      <div className={title || subtitle ? "px-6 pt-0 pb-6" : "p-6"}>
        {children}
      </div>
    </div>
  );
};

export default Card;