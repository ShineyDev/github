"""
/github/query/builtin_queries.py

    Copyright (c) 2019-2020 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

# i have tried plenty-too-many times to create a logical function
# factory here, in place of hardcoded strings - mostly for ease of
# modification. feel free to do better. it's wasting my time.

FETCH_ACTOR_AVATAR_URL = """
query fetch_actor_avatar_url ($actor_id: ID!, $size: Int=null) {
  node (id: $actor_id) {
    ... on Actor {
      avatarUrl (size: $size)
    }
  }
}
"""

FETCH_LABELABLE_LABELS = """
query fetch_labelable_labels ($labelable_id: ID!, $cursor: String=null) {
  node (id: $labelable_id) {
    ... on Labelable {
      labels (first: 10, after: $cursor) {
        nodes {
          __typename
          color
          createdAt
          description
          id
          isDefault
          name
          resourcePath
          updatedAt
          url
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_PROFILEOWNER_EMAIL = """
query fetch_profileowner_email ($profileowner_id: ID!) {
  node (id: $profileowner_id) {
    ... on ProfileOwner {
      email
    }
    ... on Mannequin {
      email
    }
  }
}
"""

FETCH_PROJECTOWNER_PROJECT = """
query fetch_projectowner_project ($projectowner_id: ID!, $project_number: Int!) {
  node (id: $projectowner_id) {
    ... on ProjectOwner {
      project (number: $project_number) {
        __typename
        body
        bodyHTML
        closed
        closedAt
        createdAt
        databaseId
        id
        name
        number
        resourcePath
        state
        updatedAt
        url
        viewerCanUpdate
      }
    }
  }
}
"""

FETCH_PROJECTOWNER_PROJECTS = """
query fetch_projectowner_projects ($projectowner_id: ID!, $cursor: String) {
  node (id: $projectowner_id) {
    ... on ProjectOwner {
      projects (first: 10, after: $cursor) {
        nodes {
          __typename
          body
          bodyHTML
          closed
          closedAt
          createdAt
          databaseId
          id
          name
          number
          resourcePath
          state
          updatedAt
          url
          viewerCanUpdate
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_REPOSITORYNODE_REPOSITORY = """
query fetch_repositorynode_repository ($repositorynode_id: ID!) {
  node (id: $repositorynode_id) {
    ... on RepositoryNode {
      repository {
        __typename
        codeOfConduct {
          __typename
          body
          id
          key
          name
          url
        }
        createdAt
        databaseId
        defaultBranchRef {
          name
        }
        description
        diskUsage
        forkCount
        hasIssuesEnabled
        hasWikiEnabled
        id
        isArchived
        isDisabled
        isFork
        isLocked
        isMirror
        isPrivate
        isTemplate
        licenseInfo {
          __typename
          body
          conditions {
            __typename
            description
            key
            label
          }
          description
          featured
          hidden
          id
          implementation
          key
          limitations {
            __typename
            description
            key
            label
          }
          name
          nickname
          permissions {
            __typename
            description
            key
            label
          }
          pseudoLicense
          spdxId
          url
        }
        lockReason
        mergeCommitAllowed
        name
        owner {
          ... on Organization {
            __typename
            anyPinnableItems
            avatarUrl
            databaseId
            description
            email
            id
            isVerified
            location
            login
            name
            newTeamResourcePath
            newTeamUrl
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            teamsResourcePath
            teamsUrl
            url
            viewerCanAdminister
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanCreateRepositories
            viewerCanCreateTeams
            viewerIsAMember
            websiteUrl
          }
          ... on User {
            __typename
            anyPinnableItems
            avatarUrl
            bio
            company
            createdAt
            databaseId
            id
            isBountyHunter
            isCampusExpert
            isDeveloperProgramMember
            isEmployee
            isHireable
            isSiteAdmin
            isViewer
            location
            login
            name
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            updatedAt
            url
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanFollow
            viewerIsFollowing
            websiteUrl
          }
        }
        primaryLanguage {
          __typename
          color
          id
          name
        }
        pushedAt
        rebaseMergeAllowed
        resourcePath
        squashMergeAllowed
        updatedAt
        url
        viewerCanAdminister
        viewerCanCreateProjects
        viewerCanSubscribe
        viewerCanUpdateTopics
        viewerPermission
        viewerSubscription
      }
    }
  }
}
"""




FETCH_ALL_CODES_OF_CONDUCT = """
query fetch_all_codes_of_conduct {
  codesOfConduct {
    __typename
    body
    id
    key
    name
    resourcePath
    url
  }
}
"""

FETCH_ALL_LICENSES = """
query fetch_all_licenses {
  licenses {
    __typename
    body
    conditions {
      __typename
      description
      key
      label
    }
    description
    featured
    hidden
    id
    implementation
    key
    limitations {
      __typename
      description
      key
      label
    }
    name
    nickname
    permissions {
      __typename
      description
      key
      label
    }
    pseudoLicense
    spdxId
    url
  }
}
"""

FETCH_AUTHENTICATED_USER = """
query fetch_authenticated_user {
  viewer {
    __typename
    anyPinnableItems
    avatarUrl
    bio
    company
    createdAt
    databaseId
    id
    isBountyHunter
    isCampusExpert
    isDeveloperProgramMember
    isEmployee
    isHireable
    isSiteAdmin
    isViewer
    location
    login
    name
    pinnedItemsRemaining
    projectsResourcePath
    projectsUrl
    resourcePath
    updatedAt
    url
    viewerCanChangePinnedItems
    viewerCanCreateProjects
    viewerCanFollow
    viewerIsFollowing
    websiteUrl
  }
}
"""

FETCH_CODE_OF_CONDUCT = """
query fetch_code_of_conduct ($key: String!) {
  codeOfConduct (key: $key) {
    __typename
    body
    id
    key
    name
    resourcePath
    url
  }
}
"""

FETCH_LICENSE = """
query fetch_license ($key: String!) {
  license (key: $key) {
    __typename
    body
    conditions {
      __typename
      description
      key
      label
    }
    description
    featured
    hidden
    id
    implementation
    key
    limitations {
      __typename
      description
      key
      label
    }
    name
    nickname
    permissions {
      __typename
      description
      key
      label
    }
    pseudoLicense
    spdxId
    url
  }
}
"""

FETCH_METADATA = """
query fetch_metadata {
  meta {
    __typename
    gitHubServicesSha
    gitIpAddresses
    hookIpAddresses
    importerIpAddresses
    isPasswordAuthenticationVerifiable
    pagesIpAddresses
  }
}
"""

FETCH_NODE = """
query fetch_node ($id: ID!) {
  node (id: $id) {
    __typename
    id
  }
}
"""

FETCH_NODES = """
query fetch_nodes ($ids: [ID!]!) {
  nodes (ids: $ids) {
    __typename
    id
  }
}
"""

FETCH_ORGANIZATION = """
query fetch_organization ($login: String!) {
  organization (login: $login) {
    __typename
    anyPinnableItems
    avatarUrl
    databaseId
    description
    email
    id
    isVerified
    location
    login
    name
    newTeamResourcePath
    newTeamUrl
    pinnedItemsRemaining
    projectsResourcePath
    projectsUrl
    resourcePath
    teamsResourcePath
    teamsUrl
    url
    viewerCanAdminister
    viewerCanChangePinnedItems
    viewerCanCreateProjects
    viewerCanCreateRepositories
    viewerCanCreateTeams
    viewerIsAMember
    websiteUrl
  }
}
"""

FETCH_PROJECT_COLUMNS = """
query fetch_project_columns ($project_id: ID!, $cursor: String) {
  node (id: $project_id) {
    ... on Project {
      columns (first: 10, after: $cursor) {
        nodes {
          __typename
          createdAt
          databaseId
          id
          name
          purpose
          resourcePath
          updatedAt
          url
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_PROJECTCOLUMN_CARDS = """
query fetch_projectcolumn_cards ($projectcolumn_id: ID!, $cursor: String) {
  node (id: $projectcolumn_id) {
    ... on ProjectColumn {
      cards (first: 10, after: $cursor) {
        nodes {
          __typename
          createdAt
          databaseId
          id
          isArchived
          note
          resourcePath
          state
          updatedAt
          url
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_RATE_LIMIT = """
query fetch_rate_limit {
  rateLimit {
    __typename
    limit
    remaining
    resetAt
  }
}
"""

FETCH_REPOSITORY = """
query fetch_repository ($owner: String!, $name: String!) {
  repository (owner: $owner, name: $name) {
    __typename
    codeOfConduct {
      __typename
      body
      id
      key
      name
      url
    }
    createdAt
    databaseId
    defaultBranchRef {
      name
    }
    description
    diskUsage
    forkCount
    hasIssuesEnabled
    hasWikiEnabled
    id
    isArchived
    isDisabled
    isFork
    isLocked
    isMirror
    isPrivate
    isTemplate
    licenseInfo {
      __typename
      body
      conditions {
        __typename
        description
        key
        label
      }
      description
      featured
      hidden
      id
      implementation
      key
      limitations {
        __typename
        description
        key
        label
      }
      name
      nickname
      permissions {
        __typename
        description
        key
        label
      }
      pseudoLicense
      spdxId
      url
    }
    lockReason
    mergeCommitAllowed
    name
    owner {
      ... on Organization {
        __typename
        anyPinnableItems
        avatarUrl
        databaseId
        description
        email
        id
        isVerified
        location
        login
        name
        newTeamResourcePath
        newTeamUrl
        pinnedItemsRemaining
        projectsResourcePath
        projectsUrl
        resourcePath
        teamsResourcePath
        teamsUrl
        url
        viewerCanAdminister
        viewerCanChangePinnedItems
        viewerCanCreateProjects
        viewerCanCreateRepositories
        viewerCanCreateTeams
        viewerIsAMember
        websiteUrl
      }
      ... on User {
        __typename
        anyPinnableItems
        avatarUrl
        bio
        company
        createdAt
        databaseId
        id
        isBountyHunter
        isCampusExpert
        isDeveloperProgramMember
        isEmployee
        isHireable
        isSiteAdmin
        isViewer
        location
        login
        name
        pinnedItemsRemaining
        projectsResourcePath
        projectsUrl
        resourcePath
        updatedAt
        url
        viewerCanChangePinnedItems
        viewerCanCreateProjects
        viewerCanFollow
        viewerIsFollowing
        websiteUrl
      }
    }
    primaryLanguage {
      __typename
      color
      id
      name
    }
    pushedAt
    rebaseMergeAllowed
    resourcePath
    squashMergeAllowed
    updatedAt
    url
    viewerCanAdminister
    viewerCanCreateProjects
    viewerCanSubscribe
    viewerCanUpdateTopics
    viewerPermission
    viewerSubscription
  }
}
"""

FETCH_REPOSITORY_ASSIGNABLE_USERS = """
query fetch_repository_assignable_users ($repository_id: ID!, $cursor: String=null) {
  node (id: $repository_id) {
    ... on Repository {
      assignableUsers (first: 10, after: $cursor) {
        nodes {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          projectsResourcePath
          projectsUrl
          resourcePath
          updatedAt
          url
          viewerCanChangePinnedItems
          viewerCanCreateProjects
          viewerCanFollow
          viewerIsFollowing
          websiteUrl
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_REPOSITORY_COLLABORATORS = """
query fetch_repository_collaborators ($repository_id: ID!, $cursor: String=null) {
  node (id: $repository_id) {
    ... on Repository {
      collaborators (first: 10, after: $cursor) {
        nodes {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          resourcePath
          updatedAt
          url
          websiteUrl
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_REPOSITORY_ISSUE = """
query fetch_repository_issue ($repository_id: ID!, $issue_number: Int!) {
  node (id: $repository_id) {
    ... on Repository {
      issue (number: $issue_number) {
        __typename
        activeLockReason
        author {
          ... on Organization {
            __typename
            anyPinnableItems
            avatarUrl
            databaseId
            description
            email
            id
            isVerified
            location
            login
            name
            newTeamResourcePath
            newTeamUrl
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            teamsResourcePath
            teamsUrl
            url
            viewerCanAdminister
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanCreateRepositories
            viewerCanCreateTeams
            viewerIsAMember
            websiteUrl
          }
          ... on User {
            __typename
            anyPinnableItems
            avatarUrl
            bio
            company
            createdAt
            databaseId
            id
            isBountyHunter
            isCampusExpert
            isDeveloperProgramMember
            isEmployee
            isHireable
            isSiteAdmin
            isViewer
            location
            login
            name
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            updatedAt
            url
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanFollow
            viewerIsFollowing
            websiteUrl
          }
        }
        authorAssociation
        body
        bodyHTML
        bodyText
        closed
        closedAt
        createdAt
        createdViaEmail
        databaseId
        editor {
          ... on Organization {
            __typename
            anyPinnableItems
            avatarUrl
            databaseId
            description
            email
            id
            isVerified
            location
            login
            name
            newTeamResourcePath
            newTeamUrl
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            teamsResourcePath
            teamsUrl
            url
            viewerCanAdminister
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanCreateRepositories
            viewerCanCreateTeams
            viewerIsAMember
            websiteUrl
          }
          ... on User {
            __typename
            anyPinnableItems
            avatarUrl
            bio
            company
            createdAt
            databaseId
            id
            isBountyHunter
            isCampusExpert
            isDeveloperProgramMember
            isEmployee
            isHireable
            isSiteAdmin
            isViewer
            location
            login
            name
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            updatedAt
            url
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanFollow
            viewerIsFollowing
            websiteUrl
          }
        }
        id
        includesCreatedEdit
        lastEditedAt
        locked
        number
        publishedAt
        resourcePath
        state
        title
        updatedAt
        url
        viewerCanReact
        viewerCanSubscribe
        viewerCanUpdate
        viewerCannotUpdateReasons
        viewerDidAuthor
        viewerSubscription
      }
    }
  }
}
"""

FETCH_REPOSITORY_ISSUES = """
query fetch_repository_issues ($repository_id: ID!, $cursor: String=null) {
  node (id: $repository_id) {
    ... on Repository {
      issues (first: 10, after: $cursor) {
        nodes {
          __typename
          activeLockReason
          author {
            ... on Organization {
              __typename
              anyPinnableItems
              avatarUrl
              databaseId
              description
              email
              id
              isVerified
              location
              login
              name
              newTeamResourcePath
              newTeamUrl
              pinnedItemsRemaining
              projectsResourcePath
              projectsUrl
              resourcePath
              teamsResourcePath
              teamsUrl
              url
              viewerCanAdminister
              viewerCanChangePinnedItems
              viewerCanCreateProjects
              viewerCanCreateRepositories
              viewerCanCreateTeams
              viewerIsAMember
              websiteUrl
            }
            ... on User {
              __typename
              anyPinnableItems
              avatarUrl
              bio
              company
              createdAt
              databaseId
              id
              isBountyHunter
              isCampusExpert
              isDeveloperProgramMember
              isEmployee
              isHireable
              isSiteAdmin
              isViewer
              location
              login
              name
              pinnedItemsRemaining
              projectsResourcePath
              projectsUrl
              resourcePath
              updatedAt
              url
              viewerCanChangePinnedItems
              viewerCanCreateProjects
              viewerCanFollow
              viewerIsFollowing
              websiteUrl
            }
          }
          authorAssociation
          body
          bodyHTML
          bodyText
          closed
          closedAt
          createdAt
          createdViaEmail
          databaseId
          editor {
            ... on Organization {
              __typename
              anyPinnableItems
              avatarUrl
              databaseId
              description
              email
              id
              isVerified
              location
              login
              name
              newTeamResourcePath
              newTeamUrl
              pinnedItemsRemaining
              projectsResourcePath
              projectsUrl
              resourcePath
              teamsResourcePath
              teamsUrl
              url
              viewerCanAdminister
              viewerCanChangePinnedItems
              viewerCanCreateProjects
              viewerCanCreateRepositories
              viewerCanCreateTeams
              viewerIsAMember
              websiteUrl
            }
            ... on User {
              __typename
              anyPinnableItems
              avatarUrl
              bio
              company
              createdAt
              databaseId
              id
              isBountyHunter
              isCampusExpert
              isDeveloperProgramMember
              isEmployee
              isHireable
              isSiteAdmin
              isViewer
              location
              login
              name
              pinnedItemsRemaining
              projectsResourcePath
              projectsUrl
              resourcePath
              updatedAt
              url
              viewerCanChangePinnedItems
              viewerCanCreateProjects
              viewerCanFollow
              viewerIsFollowing
              websiteUrl
            }
          }
          id
          includesCreatedEdit
          lastEditedAt
          locked
          number
          publishedAt
          resourcePath
          state
          title
          updatedAt
          url
          viewerCanReact
          viewerCanSubscribe
          viewerCanUpdate
          viewerCannotUpdateReasons
          viewerDidAuthor
          viewerSubscription
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_REPOSITORY_PARENT = """
query fetch_repository_parent($repository_id: ID!) {
  node(id: $repository_id) {
    ... on Repository {
      parent {
        __typename
        codeOfConduct {
          __typename
          body
          id
          key
          name
          url
        }
        createdAt
        databaseId
        defaultBranchRef {
          name
        }
        description
        diskUsage
        forkCount
        hasIssuesEnabled
        hasWikiEnabled
        id
        isArchived
        isDisabled
        isFork
        isLocked
        isMirror
        isPrivate
        isTemplate
        licenseInfo {
          __typename
          body
          conditions {
            __typename
            description
            key
            label
          }
          description
          featured
          hidden
          id
          implementation
          key
          limitations {
            __typename
            description
            key
            label
          }
          name
          nickname
          permissions {
            __typename
            description
            key
            label
          }
          pseudoLicense
          spdxId
          url
        }
        lockReason
        mergeCommitAllowed
        name
        owner {
          ... on Organization {
            __typename
            anyPinnableItems
            avatarUrl
            databaseId
            description
            email
            id
            isVerified
            location
            login
            name
            newTeamResourcePath
            newTeamUrl
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            teamsResourcePath
            teamsUrl
            url
            viewerCanAdminister
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanCreateRepositories
            viewerCanCreateTeams
            viewerIsAMember
            websiteUrl
          }
          ... on User {
            __typename
            anyPinnableItems
            avatarUrl
            bio
            company
            createdAt
            databaseId
            id
            isBountyHunter
            isCampusExpert
            isDeveloperProgramMember
            isEmployee
            isHireable
            isSiteAdmin
            isViewer
            location
            login
            name
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            updatedAt
            url
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanFollow
            viewerIsFollowing
            websiteUrl
          }
        }
        primaryLanguage {
          __typename
          color
          id
          name
        }
        pushedAt
        rebaseMergeAllowed
        resourcePath
        squashMergeAllowed
        updatedAt
        url
        viewerCanAdminister
        viewerCanCreateProjects
        viewerCanSubscribe
        viewerCanUpdateTopics
        viewerPermission
        viewerSubscription
      }
    }
  }
}
"""

FETCH_REPOSITORY_TEMPLATE = """
query fetch_repository_template ($repository_id: ID!) {
  node (id: $repository_id) {
    ... on Repository {
      templateRepository {
        __typename
        codeOfConduct {
          __typename
          body
          id
          key
          name
          url
        }
        createdAt
        databaseId
        defaultBranchRef {
          name
        }
        description
        diskUsage
        forkCount
        hasIssuesEnabled
        hasWikiEnabled
        id
        isArchived
        isDisabled
        isFork
        isLocked
        isMirror
        isPrivate
        isTemplate
        licenseInfo {
          __typename
          body
          conditions {
            __typename
            description
            key
            label
          }
          description
          featured
          hidden
          id
          implementation
          key
          limitations {
            __typename
            description
            key
            label
          }
          name
          nickname
          permissions {
            __typename
            description
            key
            label
          }
          pseudoLicense
          spdxId
          url
        }
        lockReason
        mergeCommitAllowed
        name
        owner {
          ... on Organization {
            __typename
            anyPinnableItems
            avatarUrl
            databaseId
            description
            email
            id
            isVerified
            location
            login
            name
            newTeamResourcePath
            newTeamUrl
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            teamsResourcePath
            teamsUrl
            url
            viewerCanAdminister
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanCreateRepositories
            viewerCanCreateTeams
            viewerIsAMember
            websiteUrl
          }
          ... on User {
            __typename
            anyPinnableItems
            avatarUrl
            bio
            company
            createdAt
            databaseId
            id
            isBountyHunter
            isCampusExpert
            isDeveloperProgramMember
            isEmployee
            isHireable
            isSiteAdmin
            isViewer
            location
            login
            name
            pinnedItemsRemaining
            projectsResourcePath
            projectsUrl
            resourcePath
            updatedAt
            url
            viewerCanChangePinnedItems
            viewerCanCreateProjects
            viewerCanFollow
            viewerIsFollowing
            websiteUrl
          }
        }
        primaryLanguage {
          __typename
          color
          id
          name
        }
        pushedAt
        rebaseMergeAllowed
        resourcePath
        squashMergeAllowed
        updatedAt
        url
        viewerCanAdminister
        viewerCanCreateProjects
        viewerCanSubscribe
        viewerCanUpdateTopics
        viewerPermission
        viewerSubscription
      }
    }
  }
}
"""

FETCH_TOPIC = """
query fetch_topic ($name: String!) {
  topic (name: $name) {
    __typename
    id
    name
  }
}
"""

FETCH_TOPIC_RELATED_TOPICS = """
query fetch_topic_related_topics ($topic_id: ID!) {
  node (id: $topic_id) {
    ... on Topic {
      relatedTopics (first: 10) {
        __typename
        id
        name
      }
    }
  }
}
"""

FETCH_USER = """
query fetch_user ($login: String!) {
  user (login: $login) {
    __typename
    anyPinnableItems
    avatarUrl
    bio
    company
    createdAt
    databaseId
    id
    isBountyHunter
    isCampusExpert
    isDeveloperProgramMember
    isEmployee
    isHireable
    isSiteAdmin
    isViewer
    location
    login
    name
    pinnedItemsRemaining
    projectsResourcePath
    projectsUrl
    resourcePath
    updatedAt
    url
    viewerCanChangePinnedItems
    viewerCanCreateProjects
    viewerCanFollow
    viewerIsFollowing
    websiteUrl
  }
}
"""

FETCH_USER_COMMIT_COMMENTS = """

"""

FETCH_USER_FOLLOWERS = """
query fetch_user_followers ($user_id: ID!, $cursor: String=null) {
  node (id: $user_id) {
    ... on User {
      followers (first: 10, after: $cursor) {
        nodes {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          projectsResourcePath
          projectsUrl
          resourcePath
          updatedAt
          url
          viewerCanChangePinnedItems
          viewerCanCreateProjects
          viewerCanFollow
          viewerIsFollowing
          websiteUrl
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""

FETCH_USER_FOLLOWING = """
query fetch_user_following ($user_id: ID!, $cursor: String=null) {
  node (id: $user_id) {
    ... on User {
      following (first: 10, after: $cursor) {
        nodes {
          __typename
          anyPinnableItems
          avatarUrl
          bio
          company
          createdAt
          databaseId
          id
          isBountyHunter
          isCampusExpert
          isDeveloperProgramMember
          isEmployee
          isHireable
          isSiteAdmin
          isViewer
          location
          login
          name
          pinnedItemsRemaining
          projectsResourcePath
          projectsUrl
          resourcePath
          updatedAt
          url
          viewerCanChangePinnedItems
          viewerCanCreateProjects
          viewerCanFollow
          viewerIsFollowing
          websiteUrl
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
"""
