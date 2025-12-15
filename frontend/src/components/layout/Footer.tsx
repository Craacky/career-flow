import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-100 border-t border-gray-200 py-8">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-lg font-semibold mb-4">CareerFlow</h3>
            <p className="text-gray-600 text-sm">
              Find your dream job with our platform that connects talented professionals with great companies.
            </p>
          </div>
          
          <div>
            <h4 className="font-medium mb-4">For Job Seekers</h4>
            <ul className="space-y-2 text-sm text-gray-600">
              <li><a href="#" className="hover:text-blue-600">Browse Jobs</a></li>
              <li><a href="#" className="hover:text-blue-600">Career Resources</a></li>
              <li><a href="#" className="hover:text-blue-600">Resume Builder</a></li>
              <li><a href="#" className="hover:text-blue-600">Job Alerts</a></li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-medium mb-4">For Employers</h4>
            <ul className="space-y-2 text-sm text-gray-600">
              <li><a href="#" className="hover:text-blue-600">Post a Job</a></li>
              <li><a href="#" className="hover:text-blue-600">Browse Candidates</a></li>
              <li><a href="#" className="hover:text-blue-600">Recruiting Solutions</a></li>
              <li><a href="#" className="hover:text-blue-600">Pricing</a></li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-medium mb-4">Company</h4>
            <ul className="space-y-2 text-sm text-gray-600">
              <li><a href="#" className="hover:text-blue-600">About Us</a></li>
              <li><a href="#" className="hover:text-blue-600">Contact</a></li>
              <li><a href="#" className="hover:text-blue-600">Privacy Policy</a></li>
              <li><a href="#" className="hover:text-blue-600">Terms of Service</a></li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-200 mt-8 pt-6 text-center text-sm text-gray-500">
          © {new Date().getFullYear()} CareerFlow. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;