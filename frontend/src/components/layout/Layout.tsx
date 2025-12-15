import React from 'react';
import Header from './Header';
import Footer from './Footer';
import Container from './Container';

interface LayoutProps {
  children: React.ReactNode;
  withSidebar?: boolean;
}

const Layout: React.FC<LayoutProps> = ({ children, withSidebar = false }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <div className="flex flex-1">
        {withSidebar && (
          <aside className="hidden md:block">
            {/* Sidebar will be imported and added here */}
          </aside>
        )}
        <main className="flex-1 py-6">
          <Container>
            {children}
          </Container>
        </main>
      </div>
      <Footer />
    </div>
  );
};

export default Layout;