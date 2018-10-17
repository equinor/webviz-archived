import styled from 'styled-components';
import PropTypes from 'prop-types';

const PageWrapper = styled.div`
    margin: 20px;
`;

const Page = ({id, children}) => <PageWrapper id={id}>{children}</PageWrapper>;

Page.propTypes = {
    id: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    children: PropTypes.node,
};

export default Page;
