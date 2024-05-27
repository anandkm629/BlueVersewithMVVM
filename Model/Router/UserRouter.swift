//
//  UserRouter.swift
//  Model
//
//  Created by Nickelfox on 27/05/24.
//  Copyright © 2024 Nickelfox. All rights reserved.
//

import Foundation
import FoxAPIKit

public enum UserRouter: BaseRouter {
    case login(email: String, password: String, app: String)
    
    public var method: HTTPMethod {
        switch self {
        case .login:
            return .post
        }
        
    }
    public var path: String {
        switch self {
        case .login:
            return "/user/authenticate"
        }
    }
    
    public var keypathToMap: String? {
        switch self {
        case .login:
            return "data"
        }
    }
}
